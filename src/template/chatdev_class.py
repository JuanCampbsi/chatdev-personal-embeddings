class ChatDevClass:
    def __init__(self):
          self.__template = '''
          Você é um engenheiro de softwarer.
          Gere uma análise aprofundada buscando entender a dúvida trazendo as melhores dicas.

          A dúvida é {question}.

          Certifique-se de fornecer insights e conclusões para esta seção.
          '''
    @property
    def model(self):
      return self.__template 
          
  