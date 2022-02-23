from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import check_password
from .serialize import LoginUserSerializer

# Create your views here.


class AppLogin(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(request.data)
        user = LoginUser.objects.filter(user_id=serializer.data["user_id"]).first()
        user_pw = request.data.get('user_pw', "")

        if user is None:
            return Response(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공"))
        else:
            return Response(dict(msg="비밀번호가 틀립니다."))


class RegistUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(request.data)

        # 아이디 중복 확인
        if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
            user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
            data = dict(
                msg='이미 존재하는 아이디입니다.',
                user_id=user.user_id,
                user_pw=user.user_pw
            )
            return Response(data)

        user = serializer.create(request.data)

        return Response(LoginUserSerializer(user).data)
