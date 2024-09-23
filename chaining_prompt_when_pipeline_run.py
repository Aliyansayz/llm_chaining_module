"""
chaining_prompt_when_pipeline_run without using Library
"""

"""
prompt = "Generate movies similar to {movie} "
llm = "whatever"
pipeline = QueryPipeline(chain=[prompt, llm])
response = pipeline.run(movie= "World War Z") # Just at the time of running pipeline we chain our data

print(response)

"""



class PromptTemplate : 

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


class QueryPipeline(PromptTemplate):

    pass
    def __init__(self, chain: list):
        if len(chain) == 2:
            self.prompt = chain[0]
            self.llm = chain[1]
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

