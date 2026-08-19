"""
Problem: 71. Simplify Path
Approach: Stack with String Splitting. The algorithm splits the input path by slashes to isolate directory names and commands. It uses a stack to keep track of the current valid directory path, pushing valid directory names, popping when encountering '..', and skipping '.' or empty components. Finally, it joins the stack back together with slashes.

Time Complexity: O(N) where N is the length of the path string, as splitting and iterating takes linear time.
Space Complexity: O(N) auxiliary space to store the split array and the stack components.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        folder_stack = []
        components = path.split("/")
        
        for component in components:
            if component == "..":
                if folder_stack:
                    folder_stack.pop()
            
            elif component == "." or component == "":
                continue
            else:
                folder_stack.append(component)
                
        return "/" + "/".join(folder_stack)