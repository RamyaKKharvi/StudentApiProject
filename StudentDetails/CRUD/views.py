import json
from django.http import JsonResponse
from .models import Student
from django.views.generic.base import View
from django.core.exceptions import ValidationError


class StudentCreateAndRetrieve(View):

    def get(self, request, *args, **kwargs):
        get_student_data = list(Student.objects.all().values())
        if get_student_data:
            return JsonResponse(data=get_student_data, safe=False, status=200)
        else:
            return JsonResponse(data={'success': 'No Records Found'}, status=200)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if data:
                student = Student(**data)
                student.save()
                response_data = {'id': student.id, 'message': 'Data created'}
                return JsonResponse(data=response_data, status=201)
            else:
                return JsonResponse(data={'bad_request': 'No payload'}, status=400)

        except ValidationError as e:
            return JsonResponse(data={'error': dict(e)}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


class StudentDeleteAndUpdate(View):

    def delete(self, request, student_id, **kwargs):
        student = Student.objects.filter(pk=student_id)
        if student:
            student.delete()
            return JsonResponse(data={'success': f'Record with id = {student_id} is deleted'}, status=200)
        else:
            return JsonResponse(data={'error': f'No Records with id = {student_id}'}, status=400)

    def patch(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            data = json.loads(request.body)
            if student:
                for field, value in data.items():
                    setattr(student, field, value)
                student.save()
                return JsonResponse({'success': f'Record with {student_id} updated'}, status=200)
            else:
                return JsonResponse({'error': f'No Records with id = {student_id}'}, status=400)

        except ValidationError as e:
            return JsonResponse({'error': dict(e)}, status=400)

        except Exception as e:
            return JsonResponse(data={'error': str(e)}, status=400)
