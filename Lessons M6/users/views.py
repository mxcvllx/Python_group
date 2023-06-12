from drf_yasg.utils import swagger_auto_schema
from mongoengine import ValidationError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User, VerificationCode
from users.serializers import RegisterSerializer, UserSerializer, CheckEmailVerificationCodeSerializer


class RegisterView(APIView):
    queryset = User.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserSerializer)
    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckEmailVerificationCodeView(CreateAPIView):
    queryset = VerificationCode.objects.all()
    serializer_class = CheckEmailVerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        code = serializer.validated_data.get("code")
        verification_code = self.get_queryset().filter(email=email, is_verified=False).order_by(
            "-last_sent_time").first()
        if verification_code and verification_code.code != code and verification_code.is_expire:
            raise ValidationError("Verification code invalid.")
        verification_code.is_verified = True
        verification_code.save(update_fields=["is_verified"])
        return Response({"detail": "Verification code is verified."})


class CheckEmailVerificationCodeWithParams(APIView):

    def get(self, request, *args, **kwargs):
        email = request.query_params.get("email")
        code = request.query_params.get("code")
        verification_code = (
            VerificationCode.objects.filter(email=email, is_verified=False).order_by("-last_sent_time").first()
        )
        if verification_code and verification_code.code != code:
            raise ValidationError("Verification code invalid.")
        verification_code.is_verified = True
        verification_code.save(update_fields=["is_verified"])
        return Response({"detail": "Verification code is verified."})
