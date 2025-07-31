# -*- coding: utf-8 -*-

"""
Modul ini mensimulasikan pembacaan data dari sensor biometrik.
"""

import random
import time

class BiometricSensor:
    """
    Mensimulasikan sensor biometrik yang membaca data seperti detak jantung dan tingkat kelelahan.
    """
    def __init__(self, user_id):
        """
        Menginisialisasi simulator sensor untuk pengguna tertentu.

        Args:
            user_id (str): ID pengguna yang datanya sedang disimulasikan.
        """
        self.user_id = user_id
        # Inisialisasi status dasar untuk konsistensi simulasi
        random.seed(user_id)

    def get_stress_level(self):
        """
        Mensimulasikan tingkat stres berdasarkan detak jantung (detak per menit).
        Stres dianggap tinggi jika detak jantung > 100 bpm.

        Returns:
            int: Detak jantung yang disimulasikan.
        """
        # Simulasikan fluktuasi detak jantung
        base_hr = 80
        stress_factor = (time.time() % 60) / 60  # Fluktuasi berdasarkan waktu
        simulated_hr = base_hr + (random.uniform(-10, 10)) + (stress_factor * 40)
        return int(simulated_hr)

    def get_fatigue_level(self):
        """
        Mensimulasikan tingkat kelelahan pada skala 1 hingga 10.

        Returns:
            int: Tingkat kelelahan yang disimulasikan.
        """
        # Simulasikan kelelahan yang berfluktuasi secara perlahan
        fatigue = 5 + (random.uniform(-2, 2)) + ((time.time() % 120) / 120 * 4)
        return min(10, max(1, int(fatigue)))

    def get_biometric_data(self):
        """
        Mengambil snapshot data biometrik saat ini.

        Returns:
            dict: Kamus yang berisi data biometrik.
        """
        return {
            "timestamp": time.time(),
            "heart_rate": self.get_stress_level(),
            "fatigue_level": self.get_fatigue_level()
        }
