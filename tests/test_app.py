# -*- coding: utf-8 -*-

"""
File pengujian unit untuk aplikasi Personal Reality Filter.
"""

import unittest
import sys
import os

# Tambahkan direktori src ke path untuk mengimpor modul aplikasi
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from user_profile import UserProfile
from biometric_sensor import BiometricSensor
from reality_filter import RealityFilter

class TestUserProfile(unittest.TestCase):
    """Pengujian untuk kelas UserProfile."""

    def test_profile_creation(self):
        """Uji pembuatan profil pengguna yang berhasil."""
        user = UserProfile("test_id_123", "Test User")
        self.assertEqual(user.user_id, "test_id_123")
        self.assertEqual(user.name, "Test User")
        self.assertIsInstance(user.preferences, dict)
        self.assertIsInstance(user.biometric_history, list)

    def test_update_preference(self):
        """Uji pembaruan preferensi pengguna."""
        user = UserProfile("test_id_123", "Test User")
        user.update_preference("audio", "stress_reduction", "disabled")
        self.assertEqual(user.preferences["audio"]["stress_reduction"], "disabled")

    def test_add_biometric_record(self):
        """Uji penambahan catatan biometrik."""
        user = UserProfile("test_id_123", "Test User")
        record = {"heart_rate": 80, "fatigue": 3}
        user.add_biometric_record(record)
        self.assertEqual(len(user.biometric_history), 1)
        self.assertEqual(user.biometric_history[0], record)


class TestBiometricSensor(unittest.TestCase):
    """Pengujian untuk kelas BiometricSensor."""

    def test_get_biometric_data(self):
        """Uji format dan rentang data sensor."""
        sensor = BiometricSensor("test_user")
        data = sensor.get_biometric_data()
        self.assertIn("timestamp", data)
        self.assertIn("heart_rate", data)
        self.assertIn("fatigue_level", data)
        self.assertTrue(30 <= data["heart_rate"] <= 150)
        self.assertTrue(1 <= data["fatigue_level"] <= 10)


class TestRealityFilter(unittest.TestCase):
    """Pengujian untuk kelas RealityFilter."""

    def setUp(self):
        """Siapkan instance filter untuk setiap pengujian."""
        self.reality_filter = RealityFilter()

    def test_audio_adjustment_no_stress(self):
        """Uji penyesuaian audio saat tidak ada stres."""
        audio_data = {'high_freq_volume': 100}
        adjusted_audio = self.reality_filter.adjust_audio_for_stress(audio_data, 85)
        self.assertEqual(adjusted_audio['high_freq_volume'], 100)

    def test_audio_adjustment_with_stress(self):
        """Uji penyesuaian audio saat stres."""
        audio_data = {'high_freq_volume': 100}
        adjusted_audio = self.reality_filter.adjust_audio_for_stress(audio_data, 110)
        self.assertEqual(adjusted_audio['high_freq_volume'], 50.0)

    def test_visual_adjustment_no_fatigue(self):
        """Uji penyesuaian visual saat tidak lelah."""
        visual_data = {'text_sharpness': 5}
        adjusted_visual = self.reality_filter.adjust_visuals_for_fatigue(visual_data, 5)
        self.assertEqual(adjusted_visual['text_sharpness'], 5)

    def test_visual_adjustment_with_fatigue(self):
        """Uji penyesuaian visual saat lelah."""
        visual_data = {'text_sharpness': 5}
        adjusted_visual = self.reality_filter.adjust_visuals_for_fatigue(visual_data, 8)
        self.assertEqual(adjusted_visual['text_sharpness'], 7.0)


if __name__ == '__main__':
    unittest.main()
