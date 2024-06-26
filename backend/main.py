from application import app, api, celery

from application.api import EscalateTicketAPI, TicketAPI , UserAPI, FAQApi, ResponseAPI_by_ticket, ResponseAPI_by_response_id, ResponseAPI_by_user,TicketAll, getResolutionTimes, flaggedPostAPI, getResponseAPI_by_ticket,Login,ImportResourceUser, ResponseAPI_by_responseID_delete, CategoryAPI
from application.api import FeedbackAPI,DiscourseTopicAPI, TicketDelete,UserDelete, UnresolvedTicketsNotification, EscalatedTicketNotification, BanUsersNotifications, FetchPotentialBan, ViewFlaggedPost

api.add_resource(TicketAPI, '/api/ticket')
api.add_resource(FeedbackAPI,'/api/submitFeedback')
api.add_resource(UserAPI,'/api/user')
api.add_resource(FAQApi, '/api/faq', '/api/faq/<int:ticket_id>')
api.add_resource(ResponseAPI_by_ticket, '/api/respTicket') #For getting responses with ticket_id
api.add_resource(ResponseAPI_by_response_id, '/api/respResp') #For getting responses with response_id
api.add_resource(ResponseAPI_by_user, '/api/respUser') #For getting responses with user id.
api.add_resource(TicketAll, '/api/ticketAll') #For getting all tickets
api.add_resource(getResolutionTimes, '/api/getResolutionTimes') # For getting resolution times of support agents, only accessible to managers.
api.add_resource(flaggedPostAPI, '/api/flaggedPosts') #For getting the flagged posts.
api.add_resource(getResponseAPI_by_ticket,'/api/getResponseAPI_by_ticket') #Only for getting the responses by ticket ID
api.add_resource(Login,'/login')
api.add_resource(ImportResourceUser,'/api/importUsers')
api.add_resource(TicketDelete,'/api/ticket/<int:ticket_id>')
api.add_resource(UserDelete,'/api/user/<int:user_id>')
api.add_resource(ResponseAPI_by_responseID_delete, '/api/respRespDel/<int:responder_id>/<int:response_id>')
api.add_resource(CategoryAPI, '/api/category')
api.add_resource(EscalateTicketAPI, '/api/escalate_to_gspace')
api.add_resource(UnresolvedTicketsNotification,'/api/notifications/unresolved_tickets',  methods=['GET'])
api.add_resource(EscalatedTicketNotification, '/api/notifications/escalated_tickets', methods=['GET'])
api.add_resource(BanUsersNotifications,'/api/ban_user', methods=['POST'])
api.add_resource(FetchPotentialBan, '/api/get_flagged_users', methods=['GET'])
api.add_resource(ViewFlaggedPost, '/api/get_flagged_posts', methods=['GET'])
api.add_resource(DiscourseTopicAPI, '/api/discourse/topics')




from application.routes import *
if __name__ == '__main__':
  # Run the Flask app
  app.run(debug=True)