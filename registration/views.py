from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext_lazy as _

from registration.models import Participant


class ParticipantCreateView(SuccessMessageMixin, CreateView):
    template_name = 'registration/form.html'
    model = Participant
    fields = '__all__'
    success_url = '/zhongguo/'
    success_message = _('''Thanks for your interest!<br />
We will provide you with more details on the 'Problem solving - to awaken interest' course in early December.
<p>Wish you all the best,<br />
Opusplace team</p>''')
