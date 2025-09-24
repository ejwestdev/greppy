
Implementation of grep and regex written in Python. This is an educational project to learn more about how string matching and recursive functions work in Python. All features of grep and regex are being implemented from scratch. WIP
based on: https://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html. 

Usage:

| Syntax | Description |
|---------|-------------|
| `^` | Match from beginning of string only |
| `$` | Match at end of string |
| `char` | Match exact character |
| `.` | Match any single character |
| `*` | Match zero or more of preceding character |
| `[abc]` | Match any character in brackets |
| `[^abc]` | Match any character NOT in brackets |
| `\d` | Match any digit (0-9) |
| `\w` | Match any word character (a-z, A-Z, 0-9, _) |

example usage: 

`echo -n "1600 Pennsylvania Avenue NW, Washington, D.C." | ./my_pygrep.sh -E "\d\d\d\d Penn*`
