import sys,re
sys.path.insert(0,'work/scripts')
from audit import rows,change,write_rows
def mathematical(t):
    if '\\SGA' in t: return False
    v=re.sub(r'\\(?:operatorname|mathbb)\{[^{}]*\}','',t)
    v=re.sub(r'\\[A-Za-z]+','',v)
    words=re.findall('[A-Za-z]+',v)
    return all((len(w)==1 or w in ('nG','nH')) for w in words) and not re.search('[À-ž«»]',v) and bool(v.strip())
def fix(s, found):
    out=[];i=0
    while i<len(s):
        if s[i]!='(' or (i>0 and s[i-1]=='\\'):
            out.append(s[i]);i+=1;continue
        j=i+1;level=1
        while j<len(s) and level:
            if s[j]=='(':level+=1
            if s[j]==')':level-=1
            j+=1
        if level: out.append(s[i]);i+=1;continue
        inside=s[i+1:j-1]
        if mathematical(inside):
            found.append(inside);out.append('\\('+inside+'\\)')
        else:
            out.append('('+fix(inside,found)+')')
        i=j
    return ''.join(out)

# One-time repair of command-transport escaping; candidates were inspected
# by the principal reader against the page crops before this script ran.
for n,r in enumerate(rows(),1):
    if r['printed_page'] in ['56','57','58'] and r['kind']!='source authority':
        found=[]
        ntext=fix(r['new'],found)
        ntext=re.sub(r'_\{([ij]),s\}',lambda m:'_{'+m[1]+r'\,s}',ntext)
        ntext=ntext.replace(r'\((i=1,2)\)',r'(\(i=1,2\))')
        if found:
            change(r['file'].removeprefix('sources/'),r['printed_page'],r['new'],ntext,
                'typesetting',
                'Restore inline TeX math delimiters lost by command-string escaping in the preceding page edit; retain all formulas of the cited1970 page. For p.56 restore thin spacing, not a comma, between the two fibre indices.')
rr=rows()
for r in rr:
    if r['printed_page'] in ['56','57','58'] and r['kind'] not in ('typesetting','source authority'):
        r['confidence']='amended after second reading: original textual decisions confirmed; missing inline math delimiters repaired in following typesetting rows'
write_rows(rr)
