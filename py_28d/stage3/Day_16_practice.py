from pathlib import Path

def analyze_log(file_path):
    path = Path(file_path)
    
    # 初始化统计变量
    total_lines = 0
    error_count = 0
    longest_line = ""
    
    # 使用 with 语句安全打开文件，显式指定 encoding='utf-8' 避免乱码
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            
            # 统计包含 "ERROR" 的行数（若要严格匹配大小写或单词可根据需要调整）
            if "ERROR" in line:
                error_count += 1
                
            # 比较并记录最长的一行（去掉末尾的换行符以便准确计算长度）
            stripped_line = line.rstrip("\r\n")
            if len(stripped_line) > len(longest_line):
                longest_line = stripped_line
                
    return total_lines, error_count, longest_line

# === 测试代码 ===
if __name__ == "__main__":
    # 1. 创建一个测试日志文件用于验证
    log_file = Path("/Users/nailong/Documents/math model/数模国赛/支撑材料/problem4_2/problem4_2_报告.txt")
    # log_file.write_text(
    #     "INFO: Application started successfully.\n"
    #     "DEBUG: Loading configuration files...\n"
    #     "ERROR: Failed to connect to database!\n"
    #     "INFO: Retrying connection...\n"
    #     "ERROR: Connection timeout exceeded and critical failure occurred.\n",
    #     encoding="utf-8"
    # )
    
    # 2. 调用函数进行统计
    total, errors, longest = analyze_log(log_file)
    
    print(f"--- 日志统计结果 ---")
    print(f"总行数: {total}")
    print(f"ERROR 次数: {errors}")
    print(f"最长的一行: {longest}")
    
    # 清理测试文件
    log_file.unlink()