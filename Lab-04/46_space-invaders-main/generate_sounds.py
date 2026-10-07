import math
import os
import random
import struct
import wave

RATE = 22050


def write_wav(path, samples):
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)  # 16-bit
        w.setframerate(RATE)
        frames = b"".join(
            struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767)) for s in samples
        )
        w.writeframes(frames)


def make_fire():
    """Short descending 'pew' blip."""
    n = int(RATE * 0.15)
    samples, phase = [], 0.0
    for i in range(n):
        t = i / n
        freq = 900 - 600 * t
        phase += 2 * math.pi * freq / RATE
        wave_val = 1.0 if math.sin(phase) >= 0 else -1.0  # square wave
        samples.append(wave_val * 0.3 * (1 - t))
    return samples


def make_explosion():
    """Noise burst that fades out."""
    n = int(RATE * 0.35)
    return [random.uniform(-1, 1) * 0.5 * (1 - i / n) ** 2 for i in range(n)]


def make_game_over():
    """Four descending tones."""
    samples = []
    for freq in (400, 330, 260, 200):
        n = int(RATE * 0.22)
        for i in range(n):
            t = i / n
            samples.append(math.sin(2 * math.pi * freq * i / RATE) * 0.4 * (1 - 0.5 * t))
    return samples


if __name__ == "__main__":
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")
    os.makedirs(folder, exist_ok=True)
    write_wav(os.path.join(folder, "fire.wav"), make_fire())
    write_wav(os.path.join(folder, "explosion.wav"), make_explosion())
    write_wav(os.path.join(folder, "game_over.wav"), make_game_over())
    print("Created fire.wav, explosion.wav and game_over.wav in", folder)