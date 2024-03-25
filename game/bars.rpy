screen game_stats():
    default maxhp = 100

    vbox:
        xalign 0.005 
        yalign 0.0

        # Need at least 60%
        label _("Academic Success ({})".format(academic_points))
        bar value academic_points range maxhp xmaximum 300

        # Need at least 70%
        label _("Will to Live     ({})".format(will_to_survive_points))
        bar value will_to_survive_points range maxhp xmaximum 300

        # Need at least 50%
        label _("Relationships    ({})".format(relationship_points))
        bar value relationship_points range maxhp xmaximum 300
