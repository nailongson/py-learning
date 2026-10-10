#开始菜单
def show_menu():
    print("\n--- Todo List ---")
    print("1. 添加任务")
    print("2. 列出任务")
    print("3. 标记完成")
    print("4. 删除任务")
    print("5. 退出")

#列出（改名为 list_tasks，避免覆盖内置的 list）
def list_tasks(todo_list):
    print("今日待办事件")
    if todo_list:
    # todo_list = [
    # {"task":"写代码","status":"[未完成]"},
    # {"task":"学英语","status":"[未完成]"}
    # ]
        for i,item in enumerate(todo_list):
            print(f"{i+1}.{item['task']} {item['status']}")
    else:
        print("当前没有任务哦")

#增加
def add(todo_list):
    user_input=input("请输入要添加的待办事件: ").strip()   #去掉首尾空格，纯空格视为未输入
    if user_input:
        todo_list.append({"task": user_input, "status":"[未完成]"})
        print(f"已添加 事件 {user_input}")
    else:
        print("未输入事件")
    list_tasks(todo_list) #打印验证

#标记已完成
def mark(todo_list):
    try:
        completed_task=int(input("请输入已完成的任务的序号: "))
    except ValueError:
        print("请输入数字序号哦")
        return
    completed_task=completed_task-1
    if 0 <= completed_task < len(todo_list):
        todo_list[completed_task]["status"]="[已完成]"
        print(f"已将任务{todo_list[completed_task]['task']}标记为已完成啦")   #只有成功时才提示
    else:
        print("没有这个任务哦")
    list_tasks(todo_list) #打印验证

#删除
def delete(todo_list):
    try:
        delete_task=int(input("请输入要删除的任务的序号: "))
    except ValueError:
        print("请输入数字序号哦")
        return
    delete_task=delete_task-1
    if 0 <= delete_task < len(todo_list):
        removed=todo_list.pop(delete_task)   #按下标删除，不会删错同名任务
        print(f"已将任务{removed['task']}删除了")
    else:
        print("请输入正确的序号！")
    list_tasks(todo_list) #打印验证

#选择
def main():
    todo_list=[]
    while True:
        show_menu()
        i=input("请输入你想要进行的操作序号：").strip()   #按字符串比较，输入非数字也不会崩溃
        if i == "1":
            add(todo_list)
        elif i == "2":
            list_tasks(todo_list)
        elif i == "3":
            mark(todo_list)
        elif i == "4":
            delete(todo_list)
        elif i == "5":
            print("再见！")
            break
        else:
            print("请输入正确的序号")

if __name__ == "__main__":
    main()
