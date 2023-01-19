from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class EditBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    format = StringField('Format',validators=[DataRequired()])
    num_page = StringField('Page',validators=[DataRequired()])
    submit = SubmitField('update')
    
class CreateBookForm(FlaskForm):
    
    title = StringField('Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    avg_rating = StringField('Rating',validators=[DataRequired()])
    format = StringField('Format',validators=[DataRequired()])
    img_url = StringField('Image',validators=[DataRequired()])
    num_page = StringField('Pages',validators=[DataRequired()])
    pub_id = StringField('PublisherId',validators=[DataRequired()])
    submit = SubmitField('Create')