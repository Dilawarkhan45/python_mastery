def attendance_percentage(total_classes, attended_classes):
    if total_classes <= 0:
        return 0

    return (attended_classes / total_classes) * 100