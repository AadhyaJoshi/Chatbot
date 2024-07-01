from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only=False,logic_adapters=[{
    'import_path':'chatterbot.logic.BestMatch',
    # 'default_response':'I am sorry, I dont understand',
    # 'maximum_similarity_threshold':0.90
    }])

list_to_train=[
    "hi",
    "hey there",
    "how old are you",
    "i'm omnipotent",
    "how are you",
    "i'm good, what about you"
]

chatterbotcorpusTrainer=ChatterBotCorpusTrainer(bot)
chatterbotcorpusTrainer.train('chatterbot.corpus.english')
# list_trainer=ListTrainer(bot)
# list_trainer.train(list_to_train)

# Create your views here.
def index(request):
    return render(request,'interface/home.html')

def getResponse(request):
    userMessage=request.GET.get('userMessage')
    chat_response=str(bot.get_response(userMessage))
    return HttpResponse(chat_response)