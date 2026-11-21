from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_setting
from beanie import init_beanie
from app.db.models.user_model import UserModel
from app.db.models.permissions_model import PermissionModel
from app.db.models.user_roles_model import UserRoleModel
from app.db.models.otp_model import OtpModel
from app.db.models.team_model import TeamModel
from app.db.models.team_category_model import TeamCategoryModel
from app.db.models.lead_model import LeadsModel
from app.db.models.calender_event_model import CalenderEventModel
from app.db.models.activity_model import ActivityModel
from app.db.models.communications.telephone_numbers_model import TelephoneNumbersModel

from app.db.models.task_category_model import TaskCategoryModel
from app.db.models.task_activity_model import TaskActivityModel
from app.db.models.task_status_model import TaskStatusModel
from app.db.models.task_model import TaskModel
from app.db.models.task_remark_model import TaskRemarkModel
from app.db.models.task_report_model import TaskReportModel
from app.db.models.sub_task_model import SubTaskModel
from app.db.models.task_timelog_model import TaskTimeLogModel
from app.db.models.feature_model import FeatureModel
from app.db.models.plan_model import PlanModel
from app.db.models.company_model import CompanyModel
from app.db.models.subscription_model import SubscriptionModel
from app.db.models.notification_model import NotificationModel


settings = get_setting()

Client = AsyncIOMotorClient(settings.MONGO_URI) 

db = None


async def connect_db():
    global Client, db
    
    try:
        
        db = Client[settings.DATABASE_NAME]

        await init_beanie(database=db, document_models=[UserModel, PermissionModel, UserRoleModel, OtpModel, TeamModel, TeamCategoryModel, LeadsModel, CalenderEventModel, ActivityModel, TelephoneNumbersModel, TaskCategoryModel, TaskActivityModel, TaskStatusModel, TaskModel, TaskRemarkModel, TaskReportModel, SubTaskModel, TaskTimeLogModel, FeatureModel, PlanModel, CompanyModel, SubscriptionModel, NotificationModel])
        print("Successfully connected to MongoDB and initialized Beanie")
    except Exception as e:
        print(f"failed to connect with mongodb: {e} ")



