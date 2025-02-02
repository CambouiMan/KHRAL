import customtkinter as ctk
import requests
import webbrowser
from shared import navigate_to_page

class AccessControlApp:
    def __init__(self, container):
        self.container = container
        self.create_widgets()

    def create_widgets(self):
        """Crée tous les widgets pour la page Broken Access Control."""
        self.clear_container()

        # Colonne pour l'historique
        vuln_list_frame = ctk.CTkFrame(self.container, fg_color="#1e1e1e", width=300)
        vuln_list_frame.pack(side="left", fill="y", padx=10, pady=10)

        vuln_list_label = ctk.CTkLabel(vuln_list_frame, text="Historique des vulnérabilités", text_color="white", font=("Helvetica", 16))
        vuln_list_label.pack(pady=10)

        self.vuln_list = ctk.CTkTextbox(vuln_list_frame, fg_color="#2e2e2e", text_color="white", font=("Helvetica", 14), wrap="none", state="disabled")
        self.vuln_list.pack(fill="both", expand=True)

        # Zone principale
        main_frame = ctk.CTkFrame(self.container, fg_color="#2e2e2e")
        main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Barre pour entrer l'URL
        url_frame = ctk.CTkFrame(main_frame, fg_color="#2e2e2e")
        url_frame.pack(pady=5, padx=20, anchor="n", fill="x")

        url_label = ctk.CTkLabel(url_frame, text="Entrez l'URL :", text_color="white", font=("Helvetica", 14))
        url_label.pack(side="left", padx=5)

        self.url_entry = ctk.CTkEntry(url_frame, font=("Helvetica", 14), width=400)
        self.url_entry.pack(side="left", padx=5, fill="x", expand=True)

        # Section pour les choix d'accès
        choices_frame = ctk.CTkFrame(main_frame, fg_color="#2e2e2e")
        choices_frame.pack(pady=5, padx=20, anchor="n", fill="x")

        choices_label = ctk.CTkLabel(
            choices_frame,
            text="Choisir un type d'accès (horizontal, vertical, ou non authentifié) en défilant la liste ci-dessous :",
            text_color="white",
            font=("Helvetica", 14),
        )
        choices_label.pack(anchor="nw", padx=5, pady=5)

        self.choices_textbox = ctk.CTkTextbox(
            choices_frame,
            fg_color="#1e1e1e",
            text_color="white",
            font=("Helvetica", 14),
            height=5,
            wrap="word",
            state="normal",
        )
        self.choices_textbox.pack(fill="x", pady=5)
        self.choices_textbox.insert(
            "end",
            "1. Accès Horizontal\n"
            "2. Accès Vertical\n"
            "3. Accès Non Authentifié",
        )
        self.choices_textbox.configure(state="disabled")

        self.choice_entry = ctk.CTkEntry(
            choices_frame,
            font=("Helvetica", 14),
            width=100,
            placeholder_text="Ex: 1",
        )
        self.choice_entry.pack(anchor="nw", pady=5, padx=5)

        # Zone des résultats
        results_frame = ctk.CTkFrame(main_frame, fg_color="#2e2e2e")
        results_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.results_textbox = ctk.CTkTextbox(
            results_frame,
            fg_color="#1e1e1e",
            text_color="white",
            font=("Helvetica", 14),
            wrap="word",
            state="normal",
        )
        self.results_textbox.pack(fill="both", pady=10, padx=20, expand=True)
        self.results_textbox.configure(state="disabled")

        # Boutons en bas
        bottom_frame = ctk.CTkFrame(main_frame, fg_color="#2e2e2e")
        bottom_frame.pack(side="bottom", fill="x", pady=10, padx=20)

        # Documentation bouton
        def open_documentation():
            webbrowser.open("https://owasp.org/Top10/A01_2021-Broken_Access_Control/")

        doc_button = ctk.CTkButton(bottom_frame, text="Documentation", command=open_documentation, width=150, height=40)
        doc_button.pack(side="left", padx=5)

        # Bouton pour lancer le test
        test_button = ctk.CTkButton(
            bottom_frame,
            text="Tester",
            command=self.run_test,
            fg_color="#4CAF50",
            hover_color="#388E3C",
            text_color="white",
            corner_radius=10,
            font=("Helvetica", 16),
            height=40,
        )
        test_button.pack(side="right", padx=5)

    def run_test(self):
        """Lance le test en fonction du choix de l'utilisateur."""
        url = self.url_entry.get()
        choice = self.choice_entry.get()

        # Appel à la méthode d'affichage des résultats du test en fonction du choix
        self.display_access_control_choices(url, choice)

    def display_access_control_choices(self, url, choice):
        """Affiche les résultats du test d'accès en fonction du choix de l'utilisateur."""
        self.results_textbox.configure(state="normal")
        self.results_textbox.delete("1.0", "end")
        
        try:
            if choice == "1":
                results = self.test_horizontal_access(url)
            elif choice == "2":
                results = self.test_vertical_access(url)
            elif choice == "3":
                results = self.test_unauthenticated_access(url)
            else:
                results = "Choix invalide. Veuillez entrer 1, 2 ou 3."

            self.results_textbox.insert("end", results + "\n")
            self.vuln_list.insert("end", results + "\n")
        except Exception as e:
            self.results_textbox.insert("end", f"Erreur lors du test : {str(e)}\n")
        self.results_textbox.configure(state="disabled")

    def test_horizontal_access(self, url):
        """Teste l'accès horizontal (accès non autorisé à des ressources d'autres utilisateurs)."""
        user_ids = [123, 124, 125, 126]
        session = requests.Session()  # Créer une session pour maintenir les cookies/headers entre les requêtes
        results = []

        # Se connecter avec un utilisateur normal pour générer une session authentifiée
        login_url = f"{url}/login"
        login_payload = {"username": "testuser", "password": "password123"}  # Exemple de login
        login_response = session.post(login_url, data=login_payload)
        if login_response.status_code != 200:
            results.append(f"Échec de la connexion (code {login_response.status_code})")
            return "\n".join(results)

        for user_id in user_ids:
            # Exemple d'URL avec un paramètre d'ID utilisateur
            test_url = f"{url}/profile?id={user_id}"
            response = session.get(test_url)

            if response.status_code == 200:
                # Analyse du contenu de la réponse pour vérifier l'accès aux informations sensibles
                if "account" in response.text.lower():  # Adaptable selon la page
                    results.append(f"Accès non autorisé pour l'ID {user_id}.")
                else:
                    results.append(f"Accès autorisé pour l'ID {user_id} (problème d'accès horizontal).")
            elif response.status_code == 403:
                results.append(f"Accès bloqué pour l'ID {user_id} (comportement attendu).")
            elif response.status_code == 404:
                results.append(f"Ressource non trouvée pour l'ID {user_id}.")
            else:
                results.append(f"Erreur lors de l'accès à l'ID {user_id} (code {response.status_code}).")

        return "\n".join(results)
    
    def test_vertical_access(self, url):
        """Teste l'accès vertical (accès à des ressources non autorisées)."""
        admin_url = f"{url}/admin/dashboard"  # URL réservée à un administrateur
        regular_user_url = f"{url}/user/settings"  # URL accessible à un utilisateur normal
        session = requests.Session()
        results = []

        # Se connecter avec un utilisateur régulier
        login_url = f"{url}/login"
        login_payload = {"username": "regularuser", "password": "password123"}  # Utilisateur ordinaire
        login_response = session.post(login_url, data=login_payload)
        if login_response.status_code != 200:
            results.append(f"Échec de la connexion pour utilisateur régulier (code {login_response.status_code})")
            return "\n".join(results)

        # Test d'accès à la page utilisateur normal
        response = session.get(regular_user_url)
        if response.status_code == 200:
            results.append("Accès autorisé à la page utilisateur normal (comportement attendu).")
        else:
            results.append(f"Erreur d'accès à la page utilisateur normal (code {response.status_code}).")

        # Test d'accès à la page administrateur avec un utilisateur normal
        admin_token = self.get_admin_token(url)  # Exemple pour obtenir un token administrateur
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = session.get(admin_url, headers=headers)
        if response.status_code == 200:
            results.append("Accès non autorisé à la page admin (problème d'accès vertical).")
        elif response.status_code == 403:
            results.append("Accès bloqué pour la page admin (comportement attendu).")
        elif response.status_code == 401:
            results.append("Authentification nécessaire pour accéder à la page admin (comportement attendu).")
        else:
            results.append(f"Erreur d'accès à la page admin (code {response.status_code}).")

        return "\n".join(results)

    def get_admin_token(self, url):
        """Retourne un token JWT valide pour un administrateur."""
        admin_login_url = f"{url}/login"
        admin_payload = {"username": "adminuser", "password": "adminpassword123"}
        response = requests.post(admin_login_url, data=admin_payload)
        
        if response.status_code == 200:
            return response.json().get("token")  # Supposons que le token est renvoyé en JSON
        else:
            raise Exception("Échec de la connexion en tant qu'administrateur.")

    def test_unauthenticated_access(self, url):
        """Teste l'accès non authentifié (accès sans connexion)."""
        test_url = f"{url}/profile"  # Exemple de page de profil qui nécessite une authentification
        results = []

        # Test sans authentification (sans cookies ou token)
        response = requests.get(test_url)
        if response.status_code == 200:
            results.append("Accès autorisé sans authentification (problème de sécurité).")
        elif response.status_code == 401:
            results.append("Accès bloqué sans authentification (comportement attendu).")
        else:
            results.append(f"Erreur d'accès sans authentification (code {response.status_code}).")

        return "\n".join(results)

    def clear_container(self):
        """Efface tous les widgets dans le conteneur."""
        for widget in self.container.winfo_children():
            widget.destroy()