from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    UserProfileViewSet, CategoryListAPIView,
    CategoryDetailAPIView, SubCategoryListAPIView,
    SubCategoryDetailAPIView,
    ProductListView, ProductDetailView,
    ProductImageViewSet, ReviewViewSet, RegisterView, LoginView, LogoutView
)

router = SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'images', ProductImageViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('sub_category/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('sub_category/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
