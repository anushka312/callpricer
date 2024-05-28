from django import forms
## django material for alignment

class CallPriceForm(forms.Form):
    Asset_Price = forms.FloatField(required=True, label="Asset Price", min_value=0, max_value=1e10, initial=100)
    Strike_Price = forms.FloatField(required=True, label="Strike Price", min_value=0, max_value=1e10, initial=100)
    StDev = forms.FloatField(required=True, label="Standard Deviation", min_value=0, max_value=1, initial=.2)
    Time_Years = forms.FloatField(required=True, label="Time in Years", min_value=0, max_value=3, initial=.25)
    Risk_Free_Rate = forms.FloatField(required=True, label="Risk Free Rate", min_value=0, max_value=.5, initial=.06)