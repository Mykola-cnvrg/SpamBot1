import os
for i in range(1):
    with open(f"file{i}.txt", 'w+') as file:
        file.write('hello')
    with open(f"file{i}.txt_tags.yml", 'w+') as yml:
        yml.write(f"""---
id: \"{i}\"
source: \"yann lecun\"
""")
