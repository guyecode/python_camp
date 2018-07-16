"""面试题：在进行机器部署时，需要安装一些基础软件，这些软件会有依赖关系，现在给你这些依赖关系，你写个程序输出一个正确的软件安装顺序
 example：Ps"(QQ,Socket) 表示安装 QQ依赖于Socket, (QQ,)表示安装QQ不依赖其它软件"
  依赖关系 (QQ,.NET), (Chrome,.NET),(Music,)
  一个正确的安装顺序 Music,.NET,QQ,Chrome"""

# 该题的解题思路主要使用拓扑算法，关键词：拓扑算法、Toposort、DAG
# 拓扑算法的应用范围很广，最常见的就是在各种包管理工具中，比如Ubuntu的apt，CentOS的yum，Python中的pip
# 这些工具中都使用拓扑算法来计算软件包的依赖关系
# 下面是代码实现：


def toposort(package_groups):
    """拓扑排序"""

    # 定义一个List来存储最终的安装顺序
    result = []
    # 所有已经进入安装序列的放到这个集合里
    # 因为用它只需要判断有没有，不需要知道顺序，所以使用set类型，使用list也一样，只是效率稍微低一些
    sorted = set()

    # 再定义一个内部递归函数，实际的排序逻辑也是这个函数来实现
    def sort(package, require_packages):
        # 首先判断该软件有没有依赖，也就是rest。
        # 如果rest不为空，说明有依赖，则先对它的依赖再进行排序
        if require_packages:
            # 递归调用，先解决依赖的软件包
            sort(require_packages[0], require_packages[1:])
        # 如果没有依赖，则把该软件放入到result中，并标识为已排序，这样下次再出现该软件则可以跳过了。
        if package not in sorted:
            result.append(package)
            sorted.add(package)

    # 遍历我们要安装的软件包及它的依赖，这里的packages实际就是一个或者多个软件包组成的元组
    for packages in package_groups:
        # 对软件及它的依赖们进行排序操作
        sort(packages[0], packages[1:])

    # 返回最终排好序的结果，最终的安装顺序就会照这个执行
    return result


if __name__ == '__main__':
    # 样本数据1：QQ依赖.NET， Chrome依赖.NET，Music没有依赖
    softwares = ('QQ', '.NET'), ('Chrome', '.NET'), ('Music',)
    # 正确的输出是Music, .NET, QQ, Chrome，实际上Music放在前面还是后面无所谓，因为它可以独立安装
    print(toposort(softwares))

    # 样本数据2：
    packages = ('flask', 'werkzeug', 'python'), ('scrapy', 'twisted', 'python'), ('scrapy-redis', 'scrapy')
    # 安装的顺序应该是：'python', 'werkzeug', 'flask', 'twisted', 'scrapy', 'scrapy-redis'
    print(toposort(packages))