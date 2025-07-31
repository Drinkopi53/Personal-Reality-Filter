# -*- coding: utf-8 -*-

"""
Aplikasi utama untuk Personal Reality Filter.
File ini mengintegrasikan semua modul untuk menjalankan simulasi.
"""

import time
from user_profile import UserProfile
from biometric_sensor import BiometricSensor
from reality_filter import RealityFilter

def main():
    """
    Fungsi utama untuk menjalankan simulasi Personal Reality Filter.
    """
    # 1. Inisialisasi Profil Pengguna
    user = UserProfile(user_id="user001", name="Alex")
    print(f"Memulai simulasi untuk pengguna: {user.name}")
    print("-" * 30)

    # 2. Inisialisasi Sensor dan Filter
    sensor = BiometricSensor(user.user_id)
    reality_filter = RealityFilter()

    # 3. Jalankan loop simulasi
    print("Memulai loop simulasi... (Tekan Ctrl+C untuk berhenti)")
    try:
        for i in range(10):  # Jalankan untuk 10 iterasi sebagai contoh
            # a. Dapatkan data biometrik
            bio_data = sensor.get_biometric_data()
            user.add_biometric_record(bio_data)

            heart_rate = bio_data['heart_rate']
            fatigue_level = bio_data['fatigue_level']

            print(f"\nIterasi {i+1}: Detak Jantung={heart_rate} bpm, Kelelahan={fatigue_level}/10")

            # b. Simulasikan lingkungan audio/visual awal
            current_audio = {'high_freq_volume': 100}
            current_visuals = {'text_sharpness': 5.0}

            print(f"Kondisi Awal: Audio={current_audio}, Visual={current_visuals}")

            # c. Terapkan filter
            adjusted_audio = reality_filter.adjust_audio_for_stress(current_audio.copy(), heart_rate)
            adjusted_visuals = reality_filter.adjust_visuals_for_fatigue(current_visuals.copy(), fatigue_level)

            print(f"Kondisi Disesuaikan: Audio={adjusted_audio}, Visual={adjusted_visuals}")

            time.sleep(2) # Tunggu 2 detik sebelum iterasi berikutnya

    except KeyboardInterrupt:
        print("\nSimulasi dihentikan oleh pengguna.")
    finally:
        print("-" * 30)
        print("Simulasi selesai.")
        print(f"Total {len(user.biometric_history)} catatan biometrik direkam.")

if __name__ == "__main__":
    main()
