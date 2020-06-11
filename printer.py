from octorest import OctoRest

"""Initializes a OctoRobot 
	Parameters:
	URl: string formatted IP Address. IP address of OctoRobot. 
	apiKey:  string formatted spikey of the robot. 
"""
def connect(url, apikey):
    try:
        client = OctoRest(url=url, apikey=apikey)
        return client
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()