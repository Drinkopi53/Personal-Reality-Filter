# -*- coding: utf-8 -*-

"""
Modul ini mendefinisikan kelas UserProfile untuk mengelola data dan preferensi pengguna.
"""

class UserProfile:
    """
    Mewakili profil pengguna, termasuk preferensi dan riwayat biometrik.
    """
    def __init__(self, user_id, name):
        """
        Menginisialisasi profil pengguna baru.

        Args:
            user_id (str): ID unik untuk pengguna.
            name (str): Nama pengguna.
        """
        if not user_id or not isinstance(user_id, str):
            raise ValueError("ID pengguna harus berupa string yang tidak kosong.")
        if not name or not isinstance(name, str):
            raise ValueError("Nama pengguna harus berupa string yang tidak kosong.")

        self.user_id = user_id
        self.name = name
        self.preferences = {
            "audio": {"stress_reduction": "enabled"},
            "visual": {"fatigue_sharpening": "enabled"}
        }
        self.biometric_history = []

    def update_preference(self, category, key, value):
        """
        Memperbarui preferensi pengguna.

        Args:
            category (str): Kategori preferensi (misalnya, 'audio').
            key (str): Kunci preferensi untuk diperbarui.
            value (any): Nilai baru untuk preferensi.
        """
        if category in self.preferences:
            self.preferences[category][key] = value
        else:
            raise KeyError(f"Kategori preferensi '{category}' tidak ditemukan.")

    def add_biometric_record(self, record):
        """
        Menambahkan catatan biometrik baru ke riwayat pengguna.

        Args:
            record (dict): Catatan biometrik untuk ditambahkan.
        """
        if not isinstance(record, dict):
            raise TypeError("Catatan biometrik harus berupa kamus.")
        self.biometric_history.append(record)

    def __str__(self):
        """
        Mengembalikan representasi string dari profil pengguna.
        """
        return f"UserProfile(ID: {self.user_id}, Nama: {self.name})"
