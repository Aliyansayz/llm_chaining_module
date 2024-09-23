"""
chaining_prompt_when_pipeline_run without using Library
"""


prompt = "Generate movies similar to {movie} "
llm = "whatever"
prompt_tmpl = PromptTemplate(prompt)
pipeline = QueryPipeline(chain=[prompt_tmpl, llm])
response = pipeline.run(movie= "World War Z") # Just at the time of running pipeline we chain our data

print(response)








class QueryPipeline:

    pass
    def __init__(self, chain: list):

        self.prompt = ""
        
        for element in chain:

            if isinstance(element, PromptTemplate): self.prompt = element

            elif isinstance(element, LLMtype): self.llm = element

        
        else:
            raise TypeError("Type is invalid")



    def get_llm_response(self, prompt, llm):

        pass
        response = f"here LLM API named:`{llm}` gets called and \ngive output response relevant to {prompt}"

        return response


    def run(self, **kwargs):

        prompt   = self.prompt_chaining(prompt= self.prompt , **kwargs )
        response = self.get_llm_response(prompt= prompt , llm= self.llm )

        return response

    pass





class PromptTemplate(QueryPipeline) : 

    def __init__(self, prompt):
        self.prompt = prompt


    def prompt_chaining(self, prompt, **kwargs ):
        for key, value in kwargs.items():
            # print(f"{key}: {value}")
            if f"{key}" not in prompt:
                raise KeyError( f"{key} is not valid argument to pass in prompt template" )

        formatted_string = prompt.format(**kwargs)

        print(formatted_string)
        return formatted_string
