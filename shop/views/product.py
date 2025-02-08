from django.views.generic import DetailView
from django.contrib import messages
from products.models import Product
from products.forms import ReviewForm
from django.shortcuts import redirect

class SingleProductNormalDetailView(DetailView):
    template_name = 'shop/single-product-tab-style-top.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()  # Mahsulotning barcha rasmlari
        context['reviews'] = self.object.reviews.all()  # Ushbu mahsulotga tegishli sharhlar
        context['form'] = ReviewForm()  # Yangi sharh qo‘shish formasi
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            messages.error(request, "Sharh qoldirish uchun avval login qiling.")
            return redirect("login")

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = self.object
            review.save()
            messages.success(request, "Sharhingiz muvaffaqiyatli qo‘shildi!")
            return redirect(self.object.get_absolute_url())  # Sahifani qayta yuklaydi
        else:
            messages.error(request, "Sharh yuborishda xatolik yuz berdi.")
            return self.render_to_response(self.get_context_data(form=form))
