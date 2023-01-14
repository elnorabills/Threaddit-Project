import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import QuestionListItem from "../../Questions/QuestionListItem";
import { fetchGamingQuestions } from "../../../store/questions";
import { Modal } from "../../../Modal-Context/Modal";
import QuestionCreateForm from "../../Questions/QuestionCreateForm";
import "./Gaming.css"

const Gaming = () => {
    const dispatch = useDispatch();
    const [showModal, setShowModal] = useState(false);

    const questions = Object.values(
      useSelector((state) =>
        state.questions?.pc_questions
          ? state.questions.pc_questions
          : state.questions
      )
    );

     useEffect(() => {
       dispatch(fetchGamingQuestions()).catch(async (res) => {});
     }, [dispatch]);

    return (
      <div>
        <div className="gaming-cover-photo"></div>
        <div className="my-ql-header-askScience">
          <i id="flask" className="fa-solid fa-gamepad"></i>
          <h2 className="h2-askScience">t/gaming: Threaddit Gaming</h2>
        </div>
        <div className="science-container">
          <div className="my-ql-container">
            <button
              className="cp-button-science"
              onClick={() => setShowModal(true)}
            >
              Create Post
            </button>
            {showModal && (
              <Modal onClose={() => setShowModal(false)}>
                <QuestionCreateForm setShowModal={setShowModal} />
              </Modal>
            )}
            {questions &&
              questions.map((question) => (
                <QuestionListItem question={question}></QuestionListItem>
              ))}
          </div>
          <div>
            <div className="ab-comm-blackbox">
              <h3 className="ab-comm-text">About Community</h3>
            </div>
            <div className="about-community-container">
              <div className="ab-comm-bodybox">
                <h3 className="ab-comm-body">
                  A subreddit for (almost) anything related to games - video
                  games, board games, card games, etc. (but not sports).
                </h3>
              </div>
              <div className="created-box">
                <i class="fa-solid fa-cake-candles"></i>
                <h3 className="created-text">Created Dec 4, 2022</h3>
              </div>
              <div className="ab-comm-bodybox">
                <h3 className="ab-comm-body">
                  "Related" means that posts must contain gaming-related content
                  in the link's content, or in the post's body in the case of a
                  self-post.
                </h3>
              </div>
              <button
                className="cp-button-ab-comm"
                onClick={() => setShowModal(true)}
              >
                Create Post
              </button>
              {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                  <QuestionCreateForm setShowModal={setShowModal} />
                </Modal>
              )}
            </div>
          </div>
        </div>
      </div>
    );
}

export default Gaming;
