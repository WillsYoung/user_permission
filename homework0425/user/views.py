from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User, Role, Permission


def adduser(request):
    if request.method == "GET":
        return render(request, 'add.html')

    if request.method == "POST":
        r = request.POST
        name = r['name']
        sex = 1 if r['sex'] == '男' else 0
        birth = r['birth']

        User.objects.create(
            u_name=name,
            u_sex=sex,
            u_birth=birth
        )
        return render(request, 'add.html')


def search(request):
    # 查询某个用户具备什么权限，比如杨骑星
    # user = User.objects.get(u_name='杨骑星')
    # p = user.u
    # result = p.permission_set.all
    # 判断某个用户是否有某个权限，比如判断徐磊有没有查询用户列表信息权限
    # 先找到徐磊的所有权限
    user = User.objects.get(u_name='杨超')
    p = user.u
    result = p.permission_set.all()
    for re in result:
        if re.p_name == '查询用户列表信息权限':
            print('有此权限')
            break
    # print('没有这个权限')
    return render(request, 'show_search.html', {'res': result})
