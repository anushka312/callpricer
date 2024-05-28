from django.shortcuts import render
from forms import CallPriceForm
import math
from scipy.stats import norm


def callPriceCalc(AssetPrice, StrikePrice, StDev, TimeYears, Rf):
    num1 = math.log(AssetPrice / StrikePrice)
    num2 = (Rf + (StDev ** 2) / 2) * TimeYears
    den = StDev * (TimeYears ** .5)
    d1 = (num1 + num2) / den
    d2 = d1 - StDev * (TimeYears ** .5)

    nd1 = norm.cdf(d1)
    nd2 = norm.cdf(d2)

    callPrice = AssetPrice * nd1 - StrikePrice * nd2 * math.exp((-Rf * TimeYears))
    callPrice = round(callPrice, 2)
    return callPrice


def CallPriceView(request):
    if request.method == 'GET':
        form = CallPriceForm()

        return render(request, 'html_template.html', {
            'form': form,
            'Title': 'Call Price Calculator'
        })
    else:
        # A POST request: Handle Form Upload
        form = CallPriceForm(request.POST)

        AssetPrice = float(request.POST.get('Asset_Price', ''))
        StrikePrice = float(request.POST.get('Strike_Price', ''))
        StDev = float(request.POST.get('StDev', ''))
        TimeYears = float(request.POST.get('Time_Years', ''))
        Rf = float(request.POST.get('Risk_Free_Rate', ''))

        callPrice = callPriceCalc(AssetPrice, StrikePrice, StDev, TimeYears, Rf)

        # Discounted Payback Period & Payback Period
        return render(request, 'html_template.html', {
            'form': form,
            'Title': 'Call Price Calculator',
            'value': f'Call Price is {callPrice}',
        })