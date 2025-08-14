class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        part= path.split('/')

        for i in part:
            if i=="" or i ==".":
                continue
            elif i =="..":
                if st:
                    st.pop()
            else:
                st.append(i)

        return "/"+"/".join(st)
            

        