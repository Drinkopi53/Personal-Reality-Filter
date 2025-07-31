# -*- coding: utf-8 -*-

"""
Modul ini berisi logika inti untuk menyesuaikan output audio dan visual
berdasarkan data biometrik.
"""

class RealityFilter:
    """
    Menerapkan penyesuaian pada data audio dan visual.
    """
    STRESS_THRESHOLD_HR = 100  # Denyut jantung di atas ini dianggap stres
    FATIGUE_THRESHOLD_LEVEL = 7  # Tingkat kelelahan di atas ini dianggap lelah

    def adjust_audio_for_stress(self, audio_data, heart_rate):
        """
        Menyesuaikan data audio berdasarkan tingkat stres (detak jantung).
        Jika stres, kurangi suara frekuensi tinggi.

        Args:
            audio_data (dict): Representasi data audio (misalnya, {'high_freq_volume': 100}).
            heart_rate (int): Detak jantung pengguna saat ini.

        Returns:
            dict: Data audio yang telah disesuaikan.
        """
        if not isinstance(audio_data, dict) or 'high_freq_volume' not in audio_data:
            raise ValueError("Data audio harus berupa kamus dengan kunci 'high_freq_volume'.")

        if heart_rate > self.STRESS_THRESHOLD_HR:
            # Mengurangi volume frekuensi tinggi sebesar 50% saat stres
            original_volume = audio_data.get('high_freq_volume', 100)
            adjusted_volume = original_volume * 0.5
            print(f"STRES TERDETEKSI (Detak Jantung: {heart_rate} bpm). Mengurangi suara frekuensi tinggi.")
            audio_data['high_freq_volume'] = adjusted_volume
        return audio_data

    def adjust_visuals_for_fatigue(self, visual_data, fatigue_level):
        """
        Menyesuaikan data visual berdasarkan tingkat kelelahan.
        Jika lelah, pertajam teks.

        Args:
            visual_data (dict): Representasi data visual (misalnya, {'text_sharpness': 5}).
            fatigue_level (int): Tingkat kelelahan pengguna saat ini (skala 1-10).

        Returns:
            dict: Data visual yang telah disesuaikan.
        """
        if not isinstance(visual_data, dict) or 'text_sharpness' not in visual_data:
            raise ValueError("Data visual harus berupa kamus dengan kunci 'text_sharpness'.")

        if fatigue_level > self.FATIGUE_THRESHOLD_LEVEL:
            # Meningkatkan ketajaman teks sebesar 40% saat lelah
            original_sharpness = visual_data.get('text_sharpness', 5)
            adjusted_sharpness = original_sharpness * 1.4
            print(f"KELELAHAN TERDETEKSI (Tingkat: {fatigue_level}/10). Mempertajam teks.")
            visual_data['text_sharpness'] = adjusted_sharpness
        return visual_data
