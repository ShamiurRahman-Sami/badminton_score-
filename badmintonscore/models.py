from django.db import models


class playername(models.Model):
    player_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.player_name}"


class category(models.Model):
    match_category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.match_category}"


class teamnames(models.Model):
    team_name = models.CharField(max_length=100)
    ranking = models.IntegerField()
    player = models.ManyToManyField(playername)

    def upload_logo(self, filename):
        path = 'badmintonscore/asset/photo{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_logo)

    def __str__(self):
        return f"{self.team_name}"


class match(models.Model):
    match_number = models.CharField(max_length=10, unique=True, default="")
    match_category = models.ForeignKey(category, on_delete=models.CASCADE)
    team_nameA = models.ForeignKey(teamnames, related_name='team_nameA', on_delete= models.CASCADE)
    player_nameA = models.ManyToManyField(playername, related_name="playernameA")
    team_nameB = models.ForeignKey(teamnames, related_name='team_nameB', on_delete= models.CASCADE)
    player_nameB = models.ManyToManyField(playername, related_name="playernameb")
    score_A = models.IntegerField(default=0)
    score_B = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.match_number}-{self.match_category}"
        player_A = match.objects.get(team_nameA=teamnames).player_nameA

