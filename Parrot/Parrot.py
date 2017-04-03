import multiprocessing as mp
import time, numpy, pyaudio
import pygame.mixer
DELAY_SECONDS = 1
RATE = 25000
#tested:41000 normal, 25000 for squeaky voice, 50000 for heavy voice, 36000 girl
DELAY_SIZE = 0

def feed_queue(q):
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paInt16, channels = 1, rate=RATE, input=True, frames_per_buffer=10240)

	while True:
		frame = []
		for i in xrange(10):
			frame.append(stream.read(10240))
		data_array = numpy.fromstring(''.join(frame), 'int16')
		if q.full():
			q.get_nowait()
		q.put(data_array)
		
queue = mp.Queue(maxsize=DELAY_SIZE)
p = mp.Process(target=feed_queue, args=(queue,))
p.start()
time.sleep(DELAY_SECONDS)

pygame.mixer.init()
S = pygame.mixer.Sound
print '\n'*1000
print 'Hi this is Parrot... Just make noise...'
print '\n'*10
while True:
	d = queue.get()
	S(d).play()
