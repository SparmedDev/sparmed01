from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

import sendgrid
from contact.forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            sender_name = form.cleaned_data['sender_name']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['SparMED <info@SparMED.dk>', ]
            if cc_myself:
                recipients.append('%s <%s>' % (sender_name, sender))

            sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'))

            message = sendgrid.Mail()
            message.add_to(recipients)
            message.set_subject(subject)
            message.set_text(body)
            message.set_html(body)
            message.set_from('%s <%s>' % (sender_name, sender))
            status, msg = sg.send(message)

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thanks(request):
    feedback = _("Thank you for contacting us. We will return to you as soon as possible.")

    return render(request, 'contact.html', {'feedback': feedback})
