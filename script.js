document.addEventListener("DOMContentLoaded", function () {
    updateYoutuberList(); // Mise à jour initiale lors du chargement de la page

    // Planifier la mise à jour automatique à 6h tous les jours
    setInterval(function () {
        updateYoutuberList();
    }, getTimeUntilNextUpdate());
});

function updateYoutuberList() {
    // Récupérer les données du point de terminaison de l'API du serveur
    fetch('/api/youtube-data')
        .then(response => response.json())
        .then(data => {
            const youtuberListElement = document.getElementById("youtuberList");
            youtuberListElement.innerHTML = ""; // Effacer la liste existante

            // Mettre à jour la liste avec les nouvelles données
            data.forEach((item, index) => {
                const listItem = document.createElement("li");
                listItem.textContent = `${index + 1}. ${item.snippet.title}`;
                youtuberListElement.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des données YouTube:', error);
            
            // En cas d'erreur, vous pouvez choisir de ne pas effacer la liste existante
            // ou d'afficher un message d'erreur à l'utilisateur
        });
}

function getTimeUntilNextUpdate() {
    const now = new Date();
    const updateHour = 6; // Mettre à jour à 6h
    const nextUpdate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), updateHour);

    // Si l'heure de la mise à jour est déjà passée, planifier pour le lendemain
    if (now.getHours() >= updateHour) {
        nextUpdate.setDate(nextUpdate.getDate() + 1);
    }

    return nextUpdate - now; // Temps jusqu'à la prochaine mise à jour en millisecondes
}