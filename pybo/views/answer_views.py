from datetime import datetime
from .auth_views import login_required

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import AnswerForm  # Import AnswerForm
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):
    form = AnswerForm()     # 답변 폼 생성
    question = Question.query.get_or_404(question_id)   # 질문 ID로 질문 객체 조회
    if form.validate_on_submit():   # 폼 유효성 검사
        # 폼의 content 필드를 사용하여 답변 내용 가져오기
        # content = form.content.data  
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)  # 답변 객체 생성
        question.answer_set.append(answer)  # 질문 객체에 답변 추가 (관계 이름 일치)
        db.session.commit()  # 데이터베이스에 변경 사항 저장
        # 앵커 이름에 언더스코어를 사용하여 답변 위치로 스크롤
        return redirect('{}#answer_{}'.format(
            url_for('question.detail', question_id=question_id), answer.id))
    return render_template('question/question_detail.html', question=question, form=form)


@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#answer_{}'.format(
                url_for('question.detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)

@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect('{}#answer_{}'.format(
                url_for('question.detail', question_id=answer.question.id), answer.id))

@bp.route('/vote/<int:answer_id>/')
@login_required
def vote(answer_id):
    _answer = Answer.query.get_or_404(answer_id)
    if g.user == _answer.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    # 이미 추천한 경우
    elif g.user in _answer.voter:
        flash('이미 추천하셨습니다')
    else:
        _answer.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=_answer.question.id))