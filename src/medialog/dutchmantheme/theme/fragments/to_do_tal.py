def get_taltext(self):
    tal_text = self.data['tal_text']
    body = self.view.render(tal_text)
    return body