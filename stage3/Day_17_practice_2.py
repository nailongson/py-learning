import os
import json

#开始菜单
def show_menu():
    print("\n--- Todo List ---")
    print("1. 添加任务")
    print("2. 列出任务")
    print("3. 标记完成")
    print("4. 删除任务")
    print("5. 退出")

#列出
def list_text(todo_list):
    print("今日待办事件")
    if todo_list:
   
        for i,item in enumerate(todo_list):
            print(f"{i+1}.{item['task']} {item['status']}")
    else:
        print("当前没有任务哦")

#增加
def add(todo_list):
    user_input=input("请输入要添加的待办事件: ")
    if user_input:
        todo_list.append({"task": user_input, "status":"[未完成]"})
        print(f"已添加 事件 {user_input}")
    else:
        print("未输入事件")
    for i,item in enumerate(todo_list): #打印验证
        print(f"{i+1}.{item['task']} {item['status']}")

#标记已完成
def mark(todo_list):
    completed_task=int(input("请输入已完成的任务的序号: "))
    completed_task=completed_task-1
    if 0 <= completed_task < len(todo_list):
        todo_list[completed_task]["status"]="[已完成]"
    else:
        print("没有这个任务哦")
    print(f"已将任务{ todo_list[completed_task]['task']}标记为已完成啦")
    for i,item in enumerate(todo_list): #打印验证
        print(f"{i+1}.{item['task']} {item['status']}")

#删除
def delete(todo_list):
    delete_task=int(input("请输入要删除的任务的序号: "))
    delete_task=delete_task-1
    if 0 <= delete_task < len(todo_list):
        todo_list.remove(todo_list[delete_task])
    else:
        print("请输入正确的序号！")
    print(f"已将任务{delete_task+1}删除了")
    for i,item in enumerate(todo_list): #打印验证
        print(f"{i+1}.{item['task']} {item['status']}")

#新增读档，存档
def load_todos(filename="/Users/nailong/Documents/py learning/stage3/todo.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_todos(todos, filename="/Users/nailong/Documents/py learning/stage3/todo.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)

#选择
def main():
 # 程序启动时加载
    todo_list = load_todos()
    while True:
        show_menu()
        i=int(input("请输入你想要进行的操作序号："))
        if i == 1:
            add(todo_list)
        elif i == 2:
            list_text(todo_list)
        elif i == 3:
            mark(todo_list)
        elif i == 4:
            delete(todo_list)
        elif i == 5:  
            print("再见！")
            break
        else:
            print("请输入正确的序号")
        save_todos(todo_list)


if __name__ == "__main__":
    main()
