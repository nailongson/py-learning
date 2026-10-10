from dataclasses import dataclass

# 定义一个数据类来规范统计结果的结构
@dataclass
class ScoreStats:
    average: float
    max_score: int
    fail_count: int

# 1. 数据准备函数
def get_scores_data() -> list[int]:
    """获取或返回原始成绩列表"""
    scores = [85, 59, 92, 45, 78, 63, 90, 38]
    return scores

# 2. 计算与处理函数
def calculate_stats(scores: list[int]) -> ScoreStats:
    """计算总分、平均分、最高分以及不及格人数，并返回一个 ScoreStats 对象"""
    total_score = sum(scores)
    count = len(scores)
    average_score = total_score / count if count > 0 else 0
    max_score = max(scores)
    
    # 统计不及格个数 (< 60 分)
    fail_count = 0
    for score in scores:
        if score < 60:
            fail_count += 1
            
    # 使用 dataclass 实例化对象返回，属性清晰且有类型保障
    return ScoreStats(
        average=average_score,
        max_score=max_score,
        fail_count=fail_count
    )

# 3. 输出与展示函数
def print_report(scores: list[int], stats: ScoreStats) -> None:
    """打印最终的统计结果"""
    print(f"成绩列表: {scores}")
    print(f"平均分: {stats.average:.2f}")  # 直接用点语法访问属性，比字典的字符串键更安全
    print(f"最高分: {stats.max_score}")
    print(f"不及格个数: {stats.fail_count}")

# --- 主程序调用（组织结构） ---
if __name__ == "__main__":
    # 步骤一：获取数据
    my_scores: list[int] = get_scores_data()
    
    # 步骤二：计算结果
    result_stats: ScoreStats = calculate_stats(my_scores)
    
    # 步骤三：展示报告
    print_report(my_scores, result_stats)