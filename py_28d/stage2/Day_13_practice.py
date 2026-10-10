import random        # 这是标准库 (自带的)
from faker import Faker  # 这是第三方库 (刚才用 pip 安装的)

# 初始化 Faker 对象，'zh_CN' 表示生成中文数据
fake = Faker('zh_CN')

def advanced_roll_call(k=3):
    # 1. 使用第三方库 faker 随机生成一个 20 人的班级名单
    print("正在从系统导入学生名单...")
    class_roster = []
    for _ in range(20):
        class_roster.append(fake.name()) 
    
    print(f"班级总人数: {len(class_roster)}人")
    print("-" * 30)
    
    # 2. 使用标准库 random 进行不重复点名
    selected = random.sample(class_roster, k)
    
    print(f"🎯 今日随机点名的 {k} 位同学是：")
    for i, name in enumerate(selected, 1):
        print(f"   {i}. {name}")

# 运行程序
if __name__ == "__main__":
    advanced_roll_call(3)