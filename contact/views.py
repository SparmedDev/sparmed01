from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

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

            recipients = [{
                'email': 'info@sparmed.dk',
                'name': 'SparMed'}]
            if cc_myself:
                recipients.append({
                    'email': sender,
                    'name': sender_name})

            import mandrill
            try:
                mandrill_client = mandrill.Mandrill('Bml5XQ7DhMZLvw3NDwykrQ')
                message = {
                    'from_email': sender,
                    'from_name': sender_name,
                    'subject': subject,
                    'text': message,
                    'to': recipients,
                }
                result = mandrill_client.messages.send(message=message)

            except mandrill.Error, e:
                # Mandrill errors are thrown as exceptions
                print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
                raise

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thanks(request):
    feedback = _("Thank you for contacting us. We will return to you as soon as possible.")

    return render(request, 'contact.html', {'feedback': feedback})
