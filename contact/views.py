from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.mail import send_mail

from contact.forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            sender_name = form.cleaned_data['sender_name']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['SparMED <info@SparMED.dk>', ]
            if cc_myself:
                recipients.append('%s <%s>' % (sender_name, sender))

            send_mail(subject, message, '%s <%s>' % (sender_name, sender), recipients, fail_silently=False)

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thanks(request):
    feedback = _("Thank you for contacting us. We will return to you as soon as possible.")

    return render(request, 'contact.html', {'feedback': feedback})
