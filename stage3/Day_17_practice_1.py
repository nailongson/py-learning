import json
import os

def show_menu():
    print("\n--- Todo List ---")
    print("1. 添加任务")
    print("2. 列出任务")
    print("3. 标记完成")
    print("4. 删除任务")
    print("5. 退出")

#增加
def add_task(todos):
    task_name = input("请输入任务内容: ").strip()
    if task_name:
        todos.append({"task": task_name, "completed": False})
        print(f"已成功添加任务: {task_name}")
    else:
        print("任务内容不能为空！")

#列出
def list_tasks(todos):
    if not todos:
        print("当前没有待办事项。")
        return
    print("\n当前任务列表:")
    for index, item in enumerate(todos):
        status = "[已完成]" if item["completed"] else "[未完成]"
        print(f"{index + 1}. {status} {item['task']}")

#标记已完成
def complete_task(todos):
    list_tasks(todos)
    try:
        choice = int(input("请输入要标记为完成的任务编号: ")) - 1   #减一是因为列表从一开始l[0],l[1]
        if 0 <= choice < len(todos):
            todos[choice]["completed"] = True
            print(f"任务 '{todos[choice]['task']}' 已标记为完成。")
        else:
            print("编号超出范围。")
    except ValueError:
        print("请输入有效的数字编号。")

#删
def delete_task(todos):
    list_tasks(todos)
    try:
        choice = int(input("请输入要删除的任务编号: ")) - 1
        if 0 <= choice < len(todos):
            removed = todos.pop(choice)
            print(f"已删除任务: {removed['task']}")
        else:
            print("编号超出范围。")
    except ValueError:
        print("请输入有效的数字编号。")

#新增读档，存档
def load_todos(filename="todo.json"):
    filename =r"/User/nailong/Document/py learning/stage3/todo.json"
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_todos(todos, filename="todo.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)

#选择
def main():
    # 程序启动时加载
    todos = load_todos()

    while True:
        show_menu()
        choice = input("请选择操作编号 (1-5): ").strip()
        
        if choice == '1':
            add_task(todos)
        elif choice == '2':
            list_tasks(todos)
        elif choice == '3':
            complete_task(todos)
        elif choice == '4':
            delete_task(todos)
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效的选项，请重新输入。")
        save_todos(todos)



if __name__ == "__main__":
    main()