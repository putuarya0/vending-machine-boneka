import tkinter as tk
import time # Untuk jeda simulasi

# ==============================================================================
# BAGIAN 1: INISIASI (Kode Anda)
# ==============================================================================
items = {
    'A1': {'nama': 'boneka beruang', 'harga': 50000}, 'A2': {'nama': 'boneka kelinci', 'harga': 50000}, 'A3': {'nama': 'boneka penguin', 'harga': 50000},
    'B1': {'nama': 'boneka beruang', 'aksesoris':'dress', 'harga': 70000}, 'B2': {'nama': 'boneka kelinci', 'aksesoris':'dress', 'harga': 70000}, 'B3': {'nama': 'boneka penguin', 'aksesoris':'dress', 'harga': 70000},
    'C1': {'nama': 'boneka beruang', 'aksesoris':'jumpsuit', 'harga': 70000}, 'C2': {'nama': 'boneka kelinci', 'aksesoris':'jumpsuit', 'harga': 70000}, 'C3': {'nama': 'boneka penguin', 'aksesoris':'jumpsuit', 'harga': 70000},
    'D1': {'nama': 'boneka beruang', 'aksesoris':'backpack', 'harga': 70000}, 'D2': {'nama': 'boneka kelinci', 'aksesoris':'backpack', 'harga': 70000}, 'D3': {'nama': 'boneka penguin', 'aksesoris':'backpack', 'harga': 70000},
    'E1': {'nama': 'boneka beruang', 'aksesoris':'sling bag', 'harga': 70000}, 'E2': {'nama': 'boneka kelinci', 'aksesoris':'sling bag', 'harga': 70000}, 'E3': {'nama': 'boneka penguin', 'aksesoris':'sling bag', 'harga': 70000},
    'F1': {'nama': 'boneka beruang', 'aksesoris':['dress','backpack'], 'harga': 90000}, 'F2': {'nama': 'boneka kelinci', 'aksesoris':['dress','backpack'], 'harga': 90000}, 'F3': {'nama': 'boneka penguin', 'aksesoris':['dress','backpack'], 'harga': 90000},
    'G1': {'nama': 'boneka beruang', 'aksesoris':['jumpsuit','backpack'], 'harga': 90000}, 'G2': {'nama': 'boneka kelinci', 'aksesoris':['jumpsuit','backpack'], 'harga': 90000}, 'G3': {'nama': 'boneka penguin', 'aksesoris':['jumpsuit','backpack'], 'harga': 90000},
}
state_values = {'Q10k':10000, 'Q20k':20000, 'Q30k':30000, 'Q40k':40000, 'Q50k':50000, 'Q60k':60000, 'Q70k':70000, 'Q80k':80000, 'Q90k':90000}
pindah_state = { # Pastikan nama KONSISTEN (misal selalu Q50k)
    'diam':{'mulai':'pilih boneka'},
    'pilih boneka':{'pilih boneka kelinci':'boneka kelinci', 'pilih boneka beruang':'boneka beruang', 'pilih boneka penguin':'boneka penguin'},
    'boneka kelinci':{'pilih aksesoris':'aksesoris', 'tolak aksesoris':'Q50k', 'kembali':'pilih boneka'},
    'boneka beruang':{'pilih aksesoris':'aksesoris', 'tolak aksesoris':'Q50k', 'kembali':'pilih boneka'},
    'boneka penguin':{'pilih aksesoris':'aksesoris', 'tolak aksesoris':'Q50k', 'kembali':'pilih boneka'},
    'aksesoris':{'pilih jenis tas':'jenis tas', 'pilih jenis baju':'jenis baju', 'kembali':'pilih boneka'}, # Perlu state spesifik boneka jika murni
    'jenis tas':{'pilih backpack':'backpack', 'pilih sling bag':'sling bag', 'kembali':'aksesoris'},
    'backpack':{'tidak memilih aksesoris tambahan':'Q70k', 'pilih baju sebagai aksesoris tambahan':'jenis baju 2', 'kembali':'jenis tas'},
    'sling bag':{'tidak memilih aksesoris tambahan':'Q70k', 'pilih baju sebagai aksesoris tambahan':'jenis baju 2', 'kembali':'jenis tas'},
    'jenis baju':{'pilih jumpsuit':'jumpsuit', 'pilih dress':'dress', 'kembali':'aksesoris'},
    'jumpsuit':{'tidak memilih aksesoris tambahan':'Q70k', 'pilih tas sebagai aksesoris tambahan':'jenis tas 2', 'kembali':'jenis baju'},
    'dress':{'tidak memilih aksesoris tambahan':'Q70k', 'pilih tas sebagai aksesoris tambahan':'jenis tas 2', 'kembali':'jenis baju'},
    'jenis baju 2':{'pilih dress':'dress 2', 'pilih jumpsuit':'jumpsuit 2', 'kembali':'backpack'}, # Seharusnya kembali ke state tas sebelumnya
    'jenis tas 2':{'pilih backpack':'backpack 2', 'pilih sling bag':'sling bag 2', 'kembali':'jumpsuit'}, # Seharusnya kembali ke state baju sebelumnya
    'dress 2':{'lanjut pembayaran':'Q90k', 'kembali':'jenis baju 2'},
    'jumpsuit 2':{'lanjut pembayaran':'Q90k', 'kembali':'jenis baju 2'},
    'backpack 2':{'lanjut pembayaran':'Q90k', 'kembali':'jenis tas 2'},
    'sling bag 2':{'lanjut pembayaran':'Q90k', 'kembali':'jenis tas 2'},
    'Q90k':{'10000':'Q80k', '20000':'Q70k','50000':'Q40k', '100000':'kembalian_sisa_10k','batal':'diam'},
    'Q80k':{'10000':'Q70k', '20000':'Q60k','50000':'Q30k', '100000':'kembalian_sisa_20k', 'batal':'diam'},
    'Q70k':{'10000':'Q60k', '20000':'Q50k','50000':'Q20k', '100000':'kembalian_sisa_30k','batal':'diam'},
    'Q60k':{'10000':'Q50k', '20000':'Q40k','50000':'Q10k', '100000':'kembalian_sisa_40k', 'batal':'diam'},
    'Q50k':{'10000':'Q40k', '20000':'Q30k','50000':'pembayaran berhasil', '100000':'kembalian_sisa_50k','batal':'diam'},
    'Q40k':{'10000':'Q30k', '20000':'Q20k','50000':'kembalian_sisa_10k', '100000':'kembalian_sisa_60k', 'batal':'diam'},
    'Q30k':{'10000':'Q20k', '20000':'Q10k','50000':'kembalian_sisa_20k', '100000':'kembalian_sisa_70k', 'batal':'diam'},
    'Q20k':{'10000':'Q10k', '20000':'pembayaran berhasil', '50000':'kembalian_sisa_30k', '100000':'kembalian_sisa_80k', 'batal':'diam'},
    'Q10k':{'10000':'pembayaran berhasil', '20000':'kembalian_sisa_10k', '50000':'kembalian_sisa_40k', '100000':'kembalian_sisa_90k', 'batal':'diam'},
    'kembalian_sisa_10k':{'sinyal_10k_selesai':'pembayaran berhasil'},
    'kembalian_sisa_20k':{'sinyal_20k_selesai':'pembayaran berhasil'},
    'kembalian_sisa_30k':{'sinyal_20k_selesai':'kembalian_sisa_10k'},
    'kembalian_sisa_40k':{'sinyal_20k_selesai':'kembalian_sisa_20k'},
    'kembalian_sisa_50k':{'sinyal_50k_selesai':'pembayaran berhasil'},
    'kembalian_sisa_60k':{'sinyal_50k_selesai':'kembalian_sisa_10k'},
    'kembalian_sisa_70k':{'sinyal_50k_selesai':'kembalian_sisa_20k'},
    'kembalian_sisa_80k':{'sinyal_50k_selesai':'kembalian_sisa_30k'},
    'kembalian_sisa_90k':{'sinyal_50k_selesai':'kembalian_sisa_40k'},
    'pembayaran berhasil':{'sinyal_pembayaran_berhasil':'pengeluaran barang'},
    'pengeluaran barang':{'sinyal_pengeluaran_barang_berhasil':'umpan balik'},
    'umpan balik':{'sinyal_umpan_berhasil':'diam'}
}


# ==============================================================================
# BAGIAN 3: APLIKASI TKINTER LENGKAP (Kerangka)
# ==============================================================================
class VendingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mesin Boneka Mealy (Model Teoritis)")
        self.root.geometry("700x500") # Perbesar sedikit

        self.current_state = 'diam'
        self.saldo = 0
        self.target_harga = 0 # Diambil dari state_values saat masuk state Q...k
        self.current_item_details = None # Untuk menyimpan detail item yg dipilih

        # --- Variabel untuk output/tampilan ---
        self.status_text = tk.StringVar()
        self.saldo_text = tk.StringVar()
        self.info_text = tk.StringVar()
        self.item_info_text = tk.StringVar() # Untuk detail item

        # --- Frame Utama ---
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(fill="both", expand=True)

        # --- Label Status ---
        tk.Label(self.main_frame, textvariable=self.status_text, font=("Arial", 14, "bold")).pack(pady=5)
        self.item_info_label = tk.Label(self.main_frame, textvariable=self.item_info_text, font=("Arial", 12), justify=tk.LEFT)
        self.item_info_label.pack(pady=5, anchor='w')
        tk.Label(self.main_frame, textvariable=self.saldo_text, font=("Arial", 12)).pack(pady=2)
        tk.Label(self.main_frame, textvariable=self.info_text, font=("Arial", 10, "italic"), fg="blue").pack(pady=10)

        # --- Area Tombol ---
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        # --- Buat semua Frame (harus dibuat untuk SETIAP state unik) ---
        self.frames = {}
        for state_name in pindah_state.keys():
            self.frames[state_name] = tk.Frame(self.button_frame)
        # Tambahkan frame untuk state yang jadi tujuan tapi bukan kunci (jika ada)
        target_states = set(val for state_dict in pindah_state.values() for val in state_dict.values())
        for state_name in target_states:
             if state_name not in self.frames:
                 self.frames[state_name] = tk.Frame(self.button_frame)


        # Setup UI Awal
        self.update_ui()

    def handle_input(self, aksi):
        """Proses input, lakukan transisi state, dan update UI."""
        print(f"\nInput diterima: '{aksi}' dari state: '{self.current_state}'")
        self.info_text.set("") # Reset info

        if self.current_state in pindah_state and aksi in pindah_state[self.current_state]:
            next_state = pindah_state[self.current_state][aksi]
            print(f"   -> Transisi valid ke: '{next_state}'")

            # --- Logika Mealy / Aksi SEBELUM Pindah State ---
            output_message = f"OUTPUT: (Aksi '{aksi}' diterima)" # Default output

            # Reset saldo/target jika kembali ke diam
            if next_state == 'diam':
                 if self.saldo > 0 and aksi == 'batal':
                     output_message = f"OUTPUT: Transaksi Dibatalkan. Mengembalikan uang Rp{self.saldo}"
                 elif self.current_state == 'umpan balik':
                     output_message = "OUTPUT: Terima Kasih!"
                 self.saldo = 0
                 self.target_harga = 0
                 self.current_item_details = None

            # Set target harga saat memasuki state pembayaran Q...k
            elif next_state.startswith('Q') and not self.current_state.startswith('Q'):
                self.target_harga = state_values.get(next_state, 0)
                self.saldo = 0
                output_message = f"OUTPUT: Menunggu Pembayaran Rp{self.target_harga}"
                print(f"   -> Target harga di-set: {self.target_harga}")

            # Akumulasi saldo
            elif self.current_state.startswith('Q') and aksi.isdigit():
                uang_masuk = int(aksi)
                self.saldo += uang_masuk
                sisa = self.target_harga - self.saldo
                if sisa > 0 :
                     output_message = f"OUTPUT: Saldo Rp{self.saldo}. Sisa Rp{sisa}"
                else:
                     output_message = f"OUTPUT: Saldo Rp{self.saldo}. Pembayaran Cukup."
                print(f"   -> Saldo diupdate: {self.saldo}")

            # Mendapatkan detail item saat memilih boneka (asumsi input = kode item A1, A2, dll)
            # Anda perlu mengubah input di pindah_state untuk ini
            # Misal 'pilih boneka kelinci' menjadi 'A2'
            # if self.current_state == 'pilih boneka' and aksi in items:
            #      self.current_item_details = items[aksi]
            #      output_message = f"OUTPUT: Menampilkan {self.current_item_details['nama']}"

            # --- Menampilkan Output (Simulasi Aksi Mesin) ---
            self.info_text.set(output_message)

            # --- Pindah State ---
            self.current_state = next_state
            self.update_ui()
            self.trigger_internal_signals() # Cek apakah perlu sinyal internal

        else:
            print(f"   -> !!! Aksi '{aksi}' TIDAK VALID dari state '{self.current_state}' !!!")
            self.info_text.set(f"Aksi '{aksi}' tidak valid saat ini.")

    def update_ui(self):
        """Mengatur ulang tampilan (label dan tombol) sesuai state."""
        self.status_text.set(f"State: {self.current_state}")

        # Update tampilan saldo jika relevan
        if self.current_state.startswith('Q'):
            self.saldo_text.set(f"Target: Rp{self.target_harga} | Saldo Masuk: Rp{self.saldo}")
        elif self.current_state.startswith('kembalian_sisa'):
            sisa = self.current_state.split('_')[-1]
            self.saldo_text.set(f"Proses Kembalian... Sisa: Rp{sisa}")
        else:
             self.saldo_text.set("")

        # Update info item
        if self.current_item_details:
             aksesoris_str = ""
             if 'aksesoris' in self.current_item_details:
                 if isinstance(self.current_item_details['aksesoris'], list):
                     aksesoris_str = " + " + " + ".join(self.current_item_details['aksesoris'])
                 else:
                     aksesoris_str = " + " + self.current_item_details['aksesoris']
             self.item_info_text.set(f"Item: {self.current_item_details['nama']}{aksesoris_str} | Harga: Rp{self.current_item_details.get('harga','N/A')}")
        else:
             self.item_info_text.set("")


        # --- Tampilkan Frame Tombol Sesuai State ---
        # Sembunyikan semua frame tombol dulu
        for frame in self.frames.values():
            frame.pack_forget()

        # Tampilkan frame yang relevan dan isi tombolnya
        if self.current_state in self.frames:
            current_button_frame = self.frames[self.current_state]
            # Hapus tombol lama di frame ini
            for widget in current_button_frame.winfo_children():
                widget.destroy()

            # Tambahkan tombol baru berdasarkan aturan 'pindah_state'
            if self.current_state in pindah_state:
                for aksi in pindah_state[self.current_state].keys():
                    # Memberi label tombol yang lebih ramah
                    label_tombol = aksi.replace('_', ' ').title()
                    if aksi.isdigit():
                        label_tombol = f"Masukkan Rp{int(aksi):,}" # Format uang

                    tk.Button(current_button_frame, text=label_tombol,
                              command=lambda a=aksi: self.handle_input(a)).pack(side=tk.LEFT, padx=5, pady=5)

            current_button_frame.pack() # Tampilkan frame tombol yang sudah diisi

    def trigger_internal_signals(self):
        """Mensimulasikan sinyal internal setelah jeda."""
        delay = 1000 # Jeda 1 detik (ms)
        signal_input = None

        if self.current_state.startswith('kembalian_sisa'):
            output_msg = ""
            if self.current_state == 'kembalian_sisa_10k': signal_input = 'sinyal_10k_selesai'; output_msg = "Mengeluarkan 10k..."
            elif self.current_state == 'kembalian_sisa_20k': signal_input = 'sinyal_20k_selesai'; output_msg = "Mengeluarkan 20k..."
            elif self.current_state == 'kembalian_sisa_30k': signal_input = 'sinyal_20k_selesai'; output_msg = "Mengeluarkan 20k..."
            elif self.current_state == 'kembalian_sisa_40k': signal_input = 'sinyal_20k_selesai'; output_msg = "Mengeluarkan 20k..."
            elif self.current_state == 'kembalian_sisa_50k': signal_input = 'sinyal_50k_selesai'; output_msg = "Mengeluarkan 50k..."
            elif self.current_state == 'kembalian_sisa_60k': signal_input = 'sinyal_50k_selesai'; output_msg = "Mengeluarkan 50k..."
            elif self.current_state == 'kembalian_sisa_70k': signal_input = 'sinyal_50k_selesai'; output_msg = "Mengeluarkan 50k..."
            elif self.current_state == 'kembalian_sisa_80k': signal_input = 'sinyal_50k_selesai'; output_msg = "Mengeluarkan 50k..."
            elif self.current_state == 'kembalian_sisa_90k': signal_input = 'sinyal_50k_selesai'; output_msg = "Mengeluarkan 50k..."

            if signal_input:
                self.info_text.set(f"OUTPUT: {output_msg}")
                self.root.after(delay, lambda: self.handle_input(signal_input))

        elif self.current_state == 'pembayaran berhasil':
            self.info_text.set("OUTPUT: Pembayaran diverifikasi...")
            self.root.after(delay, lambda: self.handle_input('sinyal_pembayaran_berhasil'))
        elif self.current_state == 'pengeluaran barang':
             self.info_text.set("OUTPUT: Mengeluarkan barang...")
             self.root.after(delay, lambda: self.handle_input('sinyal_pengeluaran_barang_berhasil'))
        elif self.current_state == 'umpan balik':
             self.info_text.set("OUTPUT: Transaksi selesai. Terima kasih!")
             self.root.after(delay, lambda: self.handle_input('sinyal_umpan_berhasil'))

# ==============================================================================
# BAGIAN 4: MENJALANKAN APLIKASI
# ==============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineApp(root)
    root.mainloop()