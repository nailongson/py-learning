# 1. 数据准备函数（改为从键盘动态输入）
def get_scores_data():
    """通过终端输入获取学生的成绩列表"""
    scores = []
    print("请输入学生成绩（输入 q 或回车结束输入）：")
    while True:
        user_input = input("请输入成绩: ")
        # 如果用户直接回车或输入 q，则退出输入循环
        if user_input == "" or user_input.lower() == 'q':
            break
        try:
            # 将输入的字符串转换为浮点数或整数
            score = float(user_input)
            scores.append(score)
        except ValueError:
            print("输入格式有误，请输入一个有效的数字！")
            
    return scores

# 2. 计算与处理函数
def calculate_stats(scores):
    """计算总分、平均分、最高分以及不及格人数"""
    if not scores:  # 防止空列表导致报错
        return {"average": 0, "max": 0, "fail_count": 0}
        
    total_score = sum(scores)
    count = len(scores)
    average_score = total_score / count
    max_score = max(scores)
    
    # 统计不及格个数 (< 60 分)
    fail_count = 0
    for score in scores:
        if score < 60:
            fail_count += 1
            
    return {
        "average": average_score,
        "max": max_score,
        "fail_count": fail_count
    }

# 3. 输出与展示函数
def print_report(scores, stats):
    """打印最终的统计结果"""
    if not scores:
        print("没有输入任何成绩数据！")
        return
        
    print("\n--- 成绩统计报告 ---")
    print(f"成绩列表: {scores}")
    print(f"平均分: {stats['average']:.2f}")
    print(f"最高分: {stats['max']}")
    print(f"不及格个数: {stats['fail_count']}")

# --- 主程序调用（组织结构） ---
if __name__ == "__main__":
    # 步骤一：动态获取数据
    my_scores = get_scores_data()
    
    # 步骤二：计算结果
    result_stats = calculate_stats(my_scores)
    
    # 步骤三：展示报告
    print_report(my_scores, result_stats)