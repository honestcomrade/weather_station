This is the initial commit for my weather_station project.

Please check back for news and to check my progress.


		At this point I have a rough outline for the design and implementation of the project.

	The remote device will be powered via rechargeable battery and solar panel.

	It will be located outside and exchange data with wunderground's API.

	The board I've chosen is likely to be an Arduino Mega 2560, but if I can get away with using my Arduino Pro I'll try that instead.
	  I'm not sure if the processing power will be enough in that case though. Still so much to learn.

	The sensing will be performed by a host of sensors most likely included in the Sparkfun Weather shield. I'm hoping to capture measurements for the following:
	  * barometric pressure
	  * relative humidity
	  * luminosity
	  * temperature

	I'll need a wireless connection to send the results of my measurements to the web.
	Although some have certainly suggested in sticking with bluetooth modules, I'd like to try
	and work on a WiFi connection and Sparkfun's Electric Imp seems like a good tool for the job.

	The Imp runs on a C-like language they call squirrel.

		It runs two sets of software:

		The device software and the internet agent
		I think these files are saved as .nut

	The software to push data to the wunderground should be fairly simple. Just a few values being recorded at intervals and sent to the API with the right names.
	I think wiring it up will consist of a few shields with the solar cell exposed and everything else in a UV/water resistant case.

	The second aspect of the project will hopefully be a dedicated screen displaying as many pieces of data that I can from wunderground to full out the gaps which i'm not
	providing data for due to lack of sensors on my own device, and because having very up to date weather data at a moments notice (forecasts, wind speed, high/low temps)
	is extremely important to my wife.

	For the display device, I'd like to use something cheap and can power cheaply:

		The Raspberry Pi Zero is about as cheap and lightweight as it gets ($5)
	 	Running that device will require an LCD screen for output. I'm looking at the adafruit 5" 800x480 backpack for ~ $70.
		Throw in an internet connection, and stable backup power so that we always have data coming in.

	The most important data to display will be:

		* Wind speed
		* Temperature
		* Next two days forecast
		* Historical highs and lows
		* Precipitation chance
		* Sunset time

	Some fairly specific but not so-well-grasped advice I was given from a collaborator yielded the following suggestions on a mostly erased whiteboard note:

		* 1/2 Volt Solar cell
		* 2n222 - transistor on the gate
		* 10K pullup resistor from the 3.3v rail to the drain
		* Source to 5V
		* Drain to digital

Thanks for visiting my project. someday soon I will have a well mapped out repository to begin assembling the different features.
