import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


class PDFMergerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Merger")
        self.geometry("500x300")
        self.pdf_paths = []

        label = tk.Label(
            self, text="Select PDF files to merge", font=(None, 14))
        label.pack(pady=10)

        self.listbox = tk.Listbox(self, width=60, height=8)
        self.listbox.pack(padx=10, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add PDFs", command=self.add_pdfs)
        add_btn.grid(row=0, column=0, padx=5)

        remove_btn = tk.Button(
            btn_frame, text="Remove Selected", command=self.remove_selected)
        remove_btn.grid(row=0, column=1, padx=5)

        merge_btn = tk.Button(self, text="Merge and Save",
                              command=self.merge_pdfs, bg="#4caf50", fg="white")
        merge_btn.pack(pady=10, ipadx=10, ipady=5)

        self.status_label = tk.Label(
            self, text="No files selected.", fg="blue")
        self.status_label.pack(pady=5)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Choose PDF files",
            filetypes=[("PDF files", "*.pdf")]
        )
        if files:
            for f in files:
                if f not in self.pdf_paths:
                    self.pdf_paths.append(f)
                    self.listbox.insert(tk.END, f)
            self.status_label.config(
                text=f"{len(self.pdf_paths)} file(s) selected.")

    def remove_selected(self):
        selected = list(self.listbox.curselection())
        if not selected:
            return
        for index in reversed(selected):
            self.pdf_paths.pop(index)
            self.listbox.delete(index)
        self.status_label.config(
            text=f"{len(self.pdf_paths)} file(s) selected.")

    def merge_pdfs(self):
        if not self.pdf_paths:
            messagebox.showwarning(
                "No files", "Please select at least one PDF file to merge.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save merged PDF as"
        )

        if not save_path:
            return

        writer = PdfWriter()
        try:
            for path in self.pdf_paths:
                writer.append(path)
            with open(save_path, "wb") as out_file:
                writer.write(out_file)
            messagebox.showinfo(
                "Success", f"Merged PDF saved to:\n{save_path}")
            self.status_label.config(text="Merged successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")
            self.status_label.config(text="Merge failed.")


if __name__ == "__main__":
    app = PDFMergerGUI()
    app.mainloop()
