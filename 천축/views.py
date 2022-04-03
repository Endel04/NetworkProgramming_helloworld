from django.shortcuts import render

# Create your views here.
def show_란(request):
    context1 = {
        'name': '하이타니 란',
        'img_src': 'https://w.namu.la/s/5f8b8277b0ddd28c8e39252a9731cd1576c8b829d176cd23ea2ce86455d18e8af426774d144d4064855e168a654309f2a7f0e4ccd2753e8b35c9c0774926df1b1466ec2c25ed6da81f775a38abd03186',
    }
    return render(request, '천축/멤버.html', context=context1)


def show_린도(request):
    context2 = {
        'name': '하이타니 린도',
        'img_src': 'https://mblogthumb-phinf.pstatic.net/MjAyMTA4MDlfODAg/MDAxNjI4NTE5MDY1ODUy.CP5LOt1c0BNTWBBcoik2Mtr04nJb8hNPv2KXgWUO3cgg.oBB91eqSXg0UsCiEO7uTbBuGoabivIW4oVXsObaB0FIg.JPEG.karpmy91/fe62422efcd8dc63fe626a73c5c0b299.jpg?type=w800',
    }
    return render(request, '천축/멤버.html', context=context2)