import work_env 
print('Hello from repository!') 
print("New line")


def print_author(): 
    return work_env.author()

author = print_author()
print(f"Автор проекта: {author}")
    
